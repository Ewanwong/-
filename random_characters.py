import random
import sys

character_dict = {0: '预言家', 1: '女巫', 2: '猎人', 3: '守卫', 4: '盗贼', 5: '狼1', 6: '狼2',
                  7: '民', 8: '民', 9: '民', 10: '民', 11: '民', 12: '民', 13: '骑士',
                  14: '狼3', 15: '白痴'}


def shuffle_characters(num_players: int):
    assert 6 <= num_players <= 8
    character_list = [i for i in range(2 * num_players)]
    while True:
        random.shuffle(character_list)
        jinbaobao_count = 0
        lang_count = 0
        lang_yuyanjia = False
        for i in range(num_players):
            if (character_dict[character_list[2 * i]] == "预言家" and '狼' in character_dict[character_list[2*i+1]]) or ('狼' in character_dict[character_list[2 * i]] and character_dict[character_list[2*i+1]] == '预言家'):
                lang_yuyanjia = True
                break
            if character_dict[character_list[2 * i]] == "民" and character_dict[character_list[2*i+1]] == '民':
                jinbaobao_count += 1
            if (character_dict[character_list[2 * i]] == "民" and character_dict[character_list[2*i+1]] == '盗贼') or (character_dict[character_list[2 * i]] == "盗贼" and character_dict[character_list[2*i+1]] == '民'):
                jinbaobao_count += 1
            if '狼' in character_dict[character_list[2 * i]] or character_dict[character_list[2*i+1]] == '狼':
                lang_count += 1
        if lang_yuyanjia:
            continue
        if jinbaobao_count == 0:
            continue
        if lang_count == 1:
            continue
        if lang_count == 2 and num_players == 8:
            continue

        for i in range(num_players):
            print('Player'+str(i+1)+': '+str(character_dict[character_list[2*i]])+' '+str(character_dict[character_list[2*i+1]]))

        break


if __name__ == "__main__":
    shuffle_characters(int(sys.argv[1]))