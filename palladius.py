from g2pc import G2pC
from argparse import ArgumentParser
import re
from g2pc.g2pc import tone_change
import syllable_dict


class zh_phrase:

    is_zh_word = re.compile('([a-z]+)([0-9]+)')

    def __init__(self, phrase, if_capitalize) -> None:
        
        self.capitalize = if_capitalize
        self.phrase = phrase

        self.pinyin_list = self.get_pinyin_list()

    def get_pinyin_list(self) -> list:
        return [i[2] for i in g2p(self.phrase.strip())]

    def remove_tones(self) -> list:
        
        dropped_tones = []

        def helper(segment):
            reg_query = re.search(self.is_zh_word, segment)

            if reg_query is not None:
                segment = segment[:reg_query.start()] + segment[reg_query.start():reg_query.end()-1] + segment[reg_query.end():]
                helper(segment)
            else:
                dropped_tones.append(segment)

        for i in range(len(self.pinyin_list)):
            helper(self.pinyin_list[i])

        return dropped_tones

    def get_ru_list(self) -> list:

        palladiused = []
            
        for i in range(len(self.pinyin_list)):
            seg = self.pinyin_list[i]

            new_seg = ''
            if re.match('[a-z]+', seg) is not None:
                for j in re.findall('[a-z]+', seg):
                    seg = j

                    if seg[:2] not in ('zh','sh','ch'):
                        first_letter = seg[0]
                        cur_dict = eval('syllable_dict.'+first_letter)
                    else:
                        first_letters = seg[:2]
                        cur_dict = eval('syllable_dict.'+first_letters)
                    
                    new_seg += cur_dict[seg]
                # palladiused.append(new_seg + ' ')
                palladiused.append(new_seg)

            else:
                palladiused.append(seg)

        return palladiused

    def get_ru_text(self) -> str:

        ru_list = self.get_ru_list()
        # extra_spaces = re.compile('( [，。？！》”）])|([《“（] )')

        if self.capitalize:
            # ru_list = list(map(lambda word: ' ' + word[0].upper()+word[1:], ru_list))
            ru_list = list(map(lambda word: word[0].upper()+word[1:], ru_list))

        
        punct = ''.maketrans(
        {'，': ',', '。': '.', '？': '?', '、': ',', '！': '!', '：': ':', '；': ';', '（': '(', '）': ')', '“': '"',
        '”': '"', '-': '-', '《': '«', '》': '»'}) # this line has been adapted from https://github.com/pantherka
        
        # ru_string = ''.join(ru_list).strip().translate(punct).replace('  ', ' ')
        ru_string = ' '.join(ru_list).strip().translate(punct)
        return ru_string
        
            

if __name__ == "__main__":
    
    # parser = ArgumentParser()
    # parser.add_argument("-c",  action="store_true", help='Capitalize first letters of words in a string')
    # parser.add_argument("phrase")

    # args = parser.parse_args()
    # capitalize = args.c
    # phrase = args.phrase

    g2p = G2pC()

    s = zh_phrase('年至1705年，白金汉和诺曼比公爵约翰·谢菲尔德在此兴建了一处大型镇厅建筑“白金汉屋”，构成了今天的主體建築，1761年，喬治三世获得该府邸[1]，并作为一处私人寝宫。', True)

    # s = zh_phrase(phrase, capitalize)

    print(s.get_ru_text())
