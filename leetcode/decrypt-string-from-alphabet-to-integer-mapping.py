class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        mp = {
            '1' : 'a',
            '2' : 'b',
            '3' : 'c',
            '4' : 'd',
            '5' : 'e',
            '6' : 'f',
            '7' : 'g',
            '8' : 'h',
            '9' : 'i',
            '10#' : 'j',
            '11#' : 'k',
            '12#' : 'l',
            '13#' : 'm',
            '14#' : 'n',
            '15#' : 'o',
            '16#' : 'p',
            '17#' : 'q',
            '18#' : 'r',
            '19#' : 's',
            '20#' : 't',
            '21#' : 'u',
            '22#' : 'v',
            '23#' : 'w',
            '24#' : 'x',
            '25#' : 'y',
            '26#' : 'z'
        }

        ans = []
        i = len(s) - 1
        while i >= 0:
            if s[i] == '#':
                ans.append(mp[s[i-2:i+1]])
                i -= 3
            else:
                ans.append(mp[s[i]])
                i -= 1
        
        return "".join(ans[::-1])
        








        