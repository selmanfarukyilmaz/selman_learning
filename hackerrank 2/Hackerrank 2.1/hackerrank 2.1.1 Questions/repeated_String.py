def repeatedString(s: str, n: int) -> int:
    """

    :param s: String.
    :param n: The length the string must reach by repeating itself.
    :return: The answer to how many "a" words are in the resulting string.
    """
    count_a = s.count("a")

    how_many_s = int(n / len(s)) + (n % len(s) > 0)   # if n.x > n:   n = n+1
    n_mod_len_s = n % len(s)

    missing_a = 0
    if n_mod_len_s != 0:
        for i in s[n_mod_len_s:]:
            if i == "a":
                missing_a += 1
    return how_many_s * count_a - missing_a


assert repeatedString("aaaaa", 5) == 5
assert repeatedString(
    "aedbdaeaddadddcedcbbabdccbecaecaccdbebeeadadcaabbaabbaeeeecaddbcdecbbdccdebaaebecdaaabbcdeccbabaabce",
    731869010806) == 168329872486
assert repeatedString("aab", 882787) == 588525
assert repeatedString("ceebbcb", 817723) == 0
