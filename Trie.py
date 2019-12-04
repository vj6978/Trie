class TrieNode:
  def __init__(self, value):
    self.children = []
    self.value = value
    self.terminal = False

def addWord(root, word):
  if not root:
    raise Exception("No root provided!")
  else:
    temp_root = root
    for letter in word:
      for child in temp_root.children:
        if letter in child.value:
          temp_root = child
          break
      else:
        node = TrieNode(letter)
        temp_root.children.append(node)
        temp_root = node
    temp_root.terminal = True

def findWord(root, word):
  if not root:
    raise Exception("No root provided!")
  else:
    temp_root = root
    for letter in word:
      for child in temp_root.children:
        if child.value == letter:
          temp_root = child
          break
      else:
        print("The word {} does not exist in the Trie! \n".format(word))
        return -1
    print("The word {} exists in the Trie!".format(word))
    if temp_root.terminal:
      print("There are no more similar words")
    else:
      while len(temp_root.children) == 1:
        word += temp_root.children[0].value
        temp_root = temp_root.children[0]
      similar_words = []
      for child in temp_root.children:
        similar_words.append(dfs(child, word))
        print(similar_words)

def dfs(root, word):
  stack = [root]
  next_most_similar_word = ""
  similar_words = []
  while stack:
    stage = stack.pop()
    next_most_similar_word += stage.value
    for child in stage.children:
      stack.append(child)
      if child.terminal:
        similar_words.append(next_most_similar_word)
        next_most_similar_word = ""
  return similar_words

def main():
  root = TrieNode("*")
  addWord(root, "alpha")
  addWord(root, "beta")
  addWord(root, "charlie")
  addWord(root, "charlotte")
  findWord(root, "test")
  findWord(root, "char")
  findWord(root, "alphabet")

main()
