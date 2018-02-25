class StringBuilder:
    """String builder class. More efficient than concatenating strings with +"""

    def buildstring(self, words):
        """Passes through a string instead of creating a new one.
        Runtime: O(n)
        """
        return ''.join([word for word in words])
