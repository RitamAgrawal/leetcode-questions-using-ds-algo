class Solution:
    def freqAlphabets(self, s: str) -> str:
        hash_map = {'1':'a',
                    '2':'b',
                    '3':'c',
                    '4':'d',
                    '5':'e',
                    '6':'f',
                    '7':'g',
                    '8':'h',
                    '9':'i',
                    '10#':'j',
                    '11#':'k',
                    '12#':'l',
                    '13#':'m',
                    '14#':'n',
                    '15#':'o',
                    '16#':'p',
                    '17#':'q',
                    '18#':'r',
                    '19#':'s',
                    '20#':'t',
                    '21#':'u',
                    '22#':'v',
                    '23#':'w',
                    '24#':'x',
                    '25#':'y',
                    '26#':'z',
                   }
        new_string = ""
        new_list = []
        array = list(s)
        
        while array:
            key = array.pop()
            if key == "#":
                new_key = array.pop(-2)
                new_key += array.pop(-1)
                new_key += key
                new_list.append(hash_map[new_key])
            else:
                new_list.append(hash_map[key])
        
        while new_list:
            new_string += new_list.pop()
        
        return new_string  
    
    
    
    