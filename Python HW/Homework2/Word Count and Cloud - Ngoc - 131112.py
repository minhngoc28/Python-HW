import matplotlib.pyplot as plt
from wordcloud import WordCloud
import string

#1,2: Read the text file and Print a list
file_name = '/Users/macbook/Desktop/7. Python/text.txt'
with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        # Filter words that meet the conditions
        filtered_words = [word.strip(string.punctuation) for word in words
                          if len(word) >= 4 and (word[0].isupper() or word.isupper())]

        capitalized_words = {}
        for word in filtered_words:
                if word in capitalized_words:
                    capitalized_words[word] = capitalized_words[word] + 1
                else:
                    capitalized_words[word] = 1

print(capitalized_words)
for word in capitalized_words:
        print(f'{word.capitalize()}: {capitalized_words[word]}')


#3: Top 10 most common words and plot a bar chart
top_10_words = dict(sorted(capitalized_words.items(), key=lambda item: item[1], reverse=True)[:10])

plt.bar(top_10_words.keys(), top_10_words.values())
plt.xlabel('Words')
plt.ylabel('Occurrences')
plt.title('Top 10 Most Common Words')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('top_10_words_barchart.png')
plt.show()

#4.1: Generate word cloud for top filtered words
wordcloud_filtered = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_filtered)
plt.axis('off')
plt.savefig('wordcloud_filtered.png')
plt.show()

#4.2: Generate word cloud for the whole text
wordcloud_all= WordCloud(width=800, height=400, background_color='white').generate(text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud_all)
plt.axis('off')
plt.savefig('wordcloud_all.png')
plt.show()
