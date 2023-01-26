from tkinter import filedialog

path = filedialog.askopenfilename()

with open(path, encoding="utf-8-sig") as myclippings:
    all_content = myclippings.readlines()

separator = '==========\n'
note_text = 'Sua nota'
highlight_text = 'Seu destaque'
titles = []
all_notes = []
all_highlights = []
all_separator_indexes = []
books_dict = {}
text_to_txt = {}

# GET ALL THE INDEXES
for i in range(len(all_content)):
    if not all_separator_indexes:
        all_separator_indexes.append(-1)
    elif all_content[i] == separator:
        all_separator_indexes.append(i)


# CREATE THE DICT WITH ALL THE CONTENT
for i in all_separator_indexes[:-1]:
    next_i = all_separator_indexes[all_separator_indexes.index(i)+1]

    try:
        title = (all_content[i + 1].strip()).replace(":", " -")
    except:
        title = all_content[i + 1].strip()

    text = ''
    for _ in range(i + 3, next_i):
        text = text + (all_content[_]).strip() + ' '

    if title not in books_dict:
        books_dict[title] = {}

    if "Highlights" not in books_dict[title]:
        books_dict[title]["Highlights"] = {}

    if "Notes" not in books_dict[title]:
        books_dict[title]["Notes"] = {}


    if note_text in all_content[i+2]:
        note = f'nota: {all_content[i+2].split("posição")[1].split("|")[0]}'
        if note not in books_dict[title]["Notes"]:
            books_dict[title]['Notes'][note] = {}
        books_dict[title]['Notes'][note] = text

    elif highlight_text in all_content[i+2]:
        highlight = f'posição: {all_content[i+2].split("posição")[1].split("|")[0]}'
        if highlight not in books_dict[title]["Highlights"]:
            books_dict[title]['Highlights'][highlight] = {}
        books_dict[title]['Highlights'][highlight] = text


# PREPARING THE TXT
for book, details in books_dict.items():

    for number, text in books_dict[book]['Highlights'].items():
        print(number)
        try:
            number_position = int(number.split('-')[1])
        except:
            number_position = int(number.split(':')[1])

        try:
            f = int(number.split('-')[0].split(":")[1].strip())
            s = int(number.split('-')[1])
        except:
            f = int(number.split(':')[1])
            s = f
        for note_number, note_text in books_dict[book]['Notes'].items():
            n = int(note_number.split(':')[1])

            if f <= n <= s:

                txt = f"{text} — {number} - {note_number}\n\n" \
                      f"{note_text} \n\n"  \
                      "---"

                if book not in text_to_txt:
                    text_to_txt[book] = {}

                if number_position not in text_to_txt[book]:
                    text_to_txt[book][number_position] = {}
                text_to_txt[book][number_position] = txt

        if book not in text_to_txt:
            text_to_txt[book] = {}

        if number_position not in text_to_txt[book]:

                txt = f"{text} — {number}\n\n" \
                      "---"
                text_to_txt[book][number_position] = txt



# GETTING THE FIRST AND LAST DATA FOR EACH BOOK


# GENERATING THE TXT ARCHIVE
with open("@ Finished Books.txt", 'r', encoding="utf-8") as f:
   finished_books = f.readlines()
   finished_books = list(map(lambda b: b.strip(), finished_books))



   for b in text_to_txt:
       print("ok")
       if b in finished_books:
           pass
       else:
           with open("@ Finished Books.txt", 'a', encoding="utf-8") as f:
               f.write(f"{b}\n")


           with open(f"{b}.md", 'w', encoding="utf-8") as file_w:
               pass

           with open(f"{b}.md", 'r+', encoding="utf-8") as file:
               all_text = file.readlines()
               if len(all_text) == 0:
                   t = f"\n---\n" \
                        "quem: [[]]\n" \
                        "data de término:\n" \
                        "última revisão:\n" \
                       "tags: pitohat/malat-aikum🌑 fontes/livros\n" \
                       "---\n" \
                       f"## YYYY-MM-DD {b} \n\n" \
                       "### O Livro em Três Frases \n" \
                       "### O que o Livro me Acrescentou?\n"\
                       "### Notas e Comentários \n\n"
                   file.write(t)

           for pos, texto in text_to_txt[b].items():

                   with open(f"{b}.md", 'a', encoding="utf-8") as file:
                        t = texto + "\n\n"
                        file.write(t)






