from stats import get_book_text, num_words, unique_chars, sort_dict
import sys

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_text = get_book_text(sys.argv[1])
  the_dict = unique_chars(book_text)
  sorted_dict = sort_dict(the_dict)

  print("============ BOOKBOT ============\n")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(f"Found {num_words(book_text)} total words")
  print("--------- Character Count -------")
  for dict_ in sorted_dict:
    print(f"{dict_["char"]}: {dict_["num"]}")

  print("============= END ===============")


main()