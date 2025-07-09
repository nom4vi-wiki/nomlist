#!/usr/bin/env python

import csv

INPUT_FILE = 'main.csv'

def split_words(s: str):
  return s.replace('-', ' ').split(' ')

with open(INPUT_FILE, 'r', newline='', encoding='utf-8') as fd:
  reader = csv.reader(fd)
  next(reader)
  known_words: dict[tuple[str, str], int] = {}
  known_chars: dict[tuple[str, str], tuple[int, bool]] = {}
  for idx, (cqn, nom) in enumerate(reader):
    cqn = cqn.lower()
    line_no = idx + 2
    assert (n_chars := len(nom)) in (len(words := split_words(cqn)), 0), f'length mismatch at {line_no}'
    assert all(word.isalpha() for word in words), f'disallowed text in {line_no}'
    assert (pair := (cqn, nom)) not in known_words, f'duplicated entry at {line_no}, previously at {known_words[pair]}'
    if is_single_char := n_chars == 1:
      assert (char_lookup := (nom, cqn)) not in known_chars, f'redundant single-character at {line_no}, by {known_chars[char_lookup][0]}'
    known_words[pair] = line_no
    for char_def in zip(nom, words):
      if char_def in known_chars:
        assert not (prev := known_chars[char_def])[1], f'single-character at {prev[0]} now redundant by {line_no}'
        continue
      known_chars[char_def] = (line_no, is_single_char)
