import wavio
import numpy as np 
import matplotlib as mpl 
import math

sampleRate = 22050

def normalize(x):
	return (x-np.min(x))/(np.max(x)-np.min(x))

def makesin(freq, dur):

	#freq = p2f(pitch)

	# return evenly spaced numbers over the interval [0, duration] with step size of sample rate * dur
	flatSpace = np.linspace(0, dur, math.ceil(sampleRate*dur))

	# apply the sin function to the space of evenly distributed numbers.  
	sinSpace = np.sin(2 * np.pi * freq * flatSpace)

	return sinSpace

def p2f(pitch):
	freq = 2**((pitch-69)/12) * 440 # See https://en.wikipedia.org/wiki/Pitch_(music)#Labeling_pitches
	return freq

def makeChord(chord):
	# wants a "chord".
	# A chord is a tuple with the following format: (duration, pitch1, ..., pitchN)

	# define tmpChord as an empty array of length dur*samplerate
	chordOut = np.array( [0.0 for _ in range(chord[0]*sampleRate)])

	for i in range(len(chord)):
		# Loop through each index in the tuple

		# if i is 0, skip as it isn't a pitch.
		if i == 0:
			continue

		# store a numpy array with the ith pitch in the chord in tmpSin
		# sum chordOut and tmpSin.
		tmpSin = makesin(chord[i], chord[0])
		chordOut += tmpSin

	# normalize chordOut between 0 and 1 and return it
	return noramlize(chordOut)


def melodyMaker(melodyIn):
	# breakpoint()
	# expects [(dur, pitch0, ..., pitchN), (dur, pitch0, ..., pitchN)]

	#define the melody as an empty array
	melodyOut = np.array(())

	# looping through each group of stacked notes
	for chord in melodyIn:

		# define the temporary chord as an empty array
		tmpChord = np.array( [0.0 for _ in range(chord[0]*sampleRate)] )

		for i in range(len(chord)):

			# if i is 0, skip as the 0th index is for duration, not a pitch
			if i == 0:
				continue

			#breakpoint()
			# make a sine wave with the frequency at index i and the duration at the 0th index
			tmpSin = makesin(chord[i], chord[0])

			# add the sin wave to the chord.
			tmpChord += tmpSin

		melodyOut = np.concatenate((melodyOut, tmpChord))

	return normalize(melodyOut)

# define I-IV-V-I progression in C major (C-F-G-C)
song = [(1, 261.63, 329.63, 392.00), (1, 349.23, 440.00, 261.63), (1, 392.00, 440.00, 293.66), (1, 261.63, 329.63, 392.00)]
mel = melodyMaker(song)
print(mel)

wavio.write("song.wav", mel, sampleRate, sampwidth=3)