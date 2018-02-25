print('importing anagrams')

NUM_LETTERS = 26

def are_anagrams(s1, s2):
	"""
	Check if two strings are anagrams
	O(s1+s2)
	"""
	if len(s1) != len(s2):
		return False

	s1_count = get_char_count(s1.strip().lower())
	s2_count = get_char_count(s2.strip().lower())
	return char_count_diffs(s1_count, s2_count)


def get_char_count(s):
	counts = [0] * NUM_LETTERS
	offset = ord('a')

	for char in s:
		code = ord(char) - offset
		counts[code] += 1

	return counts


def char_count_diffs(s1_count, s2_count):
	if len(s1_count) != len(s2_count):
		return False
	for i in range(len(s1_count)):
		diff = s1_count[i] - s2_count[i]
		if diff != 0:
			return False
	return True


if __name__ == "__main__":
	s1 = "racecar"
	s2 = "acerarc"
	print(are_anagrams(s1, s2))
