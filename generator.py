import random


def main():
    fname, lname = get_info()
    for i in range(count):
        phone = gen_phone_number()
        vcard = make_vcard(fname, lname, phone)
        v_name = "{}.vcf".format(vcard_name())
        write_vcard(v_name, vcard)


def get_info():
    f = open("fname.txt", "r")
    f_name = f.read().split("\n")
    f.close()

    l = open("lname.txt", "r")
    l_name = l.read().split("\n")
    l.close()

    return f_name, l_name


def gen_phone_number():
    nums = []
    first = random.randint(6, 9)
    nums.extend([random.randint(0, 9) for i in range(6)])
    nums.append(333)
    return "{}{}".format(first, "".join(map(str, random.sample(nums, k=7))))


def vcard_name():
    global flag
    flag += 1
    return flag


def make_vcard(fname, lname, phone):
    first_name = random.choice(fname)
    last_name = random.choice(lname)
    return [
        'BEGIN:VCARD',
        'VERSION:4.0',
        'N:{};{}'.format(last_name, first_name),
        'FN:{} {}'.format(first_name, last_name),
        'TEL;WORK;VOICE:{}'.format(phone),
        'REV:1',
        'END:VCARD'
    ]


def write_vcard(f, vcard):
    with open(f, 'w') as f:
        f.writelines([l + '\n' for l in vcard])


if __name__ == "__main__":
    flag = 0
    count = int(input('How much card would you like to create: '))
    main()
    print('Successfully')

