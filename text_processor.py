# This script takes in raw text and returns a clean, tokenized, lemmatized text. 
# Function must be given a set {} of additional stop words. If none, give an empty set.

# Imports
import nltk
from nltk.stem import WordNetLemmatizer 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
nltk.download('stopwords')
import warnings
warnings.filterwarnings('ignore')

# Instantiate the lemmatizer
lemmatizer = WordNetLemmatizer()


# Define function to clean up text
def process_text(article, sw_custom):

    # Define a set of stopwords using `stopwords.words()`
    sw = set(stopwords.words('english'))

    # Define the regex parameters
    regex = re.compile("[^a-zA-Z ]")
    
    # Apply regex parameters to article
    re_clean = regex.sub('', article)
    
    # Apply `word_tokenize` to the regex scrubbed text
    words = word_tokenize(re_clean)
    
    # Lemmatize each word from a list of words
    lem = [lemmatizer.lemmatize(word) for word in words]
    
    # Create list of lower-case words that are not in the stopword set
    output = [word.lower() for word in lem if word.lower() not in sw.union(sw_custom)]
    
    return output