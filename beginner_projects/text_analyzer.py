"""
=============================================================================
Project 5: Text & Sentiment Lexicon Analyzer
Module: 02_beginner_projects / project5_text_analyzer.py
Description: Performs natural language text analytics, computing word count,
             sentence count, vocabulary richness, top word frequencies,
             and basic heuristic sentiment scoring.
=============================================================================
"""

import re
import sys
from collections import Counter
from typing import Dict, List, Tuple

# Common English stop words
STOP_WORDS = {
    "a", "about", "above", "after", "again", "against", "all", "am", "an",
    "and", "any", "are", "aren't", "as", "at", "be", "because", "been", "before",
    "being", "below", "between", "both", "but", "by", "can't", "cannot", "could",
    "did", "do", "does", "doing", "don't", "down", "during", "each", "few", "for",
    "from", "further", "had", "has", "have", "having", "he", "her", "here",
    "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into",
    "is", "isn't", "it", "it's", "its", "itself", "let's", "me", "more", "most",
    "my", "myself", "no", "nor", "not", "of", "off", "on", "once", "only", "or",
    "other", "ought", "our", "ours", "ourselves", "out", "over", "own", "same",
    "she", "should", "so", "some", "such", "than", "that", "the", "their",
    "theirs", "them", "themselves", "then", "there", "these", "they", "this",
    "those", "through", "to", "too", "under", "until", "up", "very", "was",
    "we", "were", "what", "when", "where", "which", "while", "who", "whom",
    "why", "with", "won't", "would", "you", "your", "yours", "yourself", "yourselves"
}

POSITIVE_WORDS = {
    "good", "great", "excellent", "amazing", "wonderful", "fantastic", "positive",
    "powerful", "innovative", "efficient", "breakthrough", "superior", "best", "promising"
}

NEGATIVE_WORDS = {
    "bad", "terrible", "poor", "difficult", "flaw", "risk", "hazard", "slow",
    "negative", "problem", "failure", "severe", "threat", "weakness", "worst"
}


class TextAnalyzer:
    def __init__(self, raw_text: str):
        self.raw_text = raw_text
        self.words = [w.lower() for w in re.findall(r"\b[a-zA-Z0-9']+\b", raw_text)]
        self.sentences = [s.strip() for s in re.split(r"[.!?]+", raw_text) if s.strip()]

    def word_count(self) -> int:
        return len(self.words)

    def character_count(self, ignore_spaces: bool = False) -> int:
        if ignore_spaces:
            return len("".join(self.raw_text.split()))
        return len(self.raw_text)

    def sentence_count(self) -> int:
        return max(1, len(self.sentences))

    def average_word_length(self) -> float:
        if not self.words:
            return 0.0
        return sum(len(w) for w in self.words) / len(self.words)

    def vocabulary_richness(self) -> float:
        """Type-Token Ratio (TTR): Unique words / Total words"""
        if not self.words:
            return 0.0
        return len(set(self.words)) / len(self.words)

    def top_keywords(self, top_n: int = 5) -> List[Tuple[str, int]]:
        filtered = [w for w in self.words if w not in STOP_WORDS and len(w) > 2]
        return Counter(filtered).most_common(top_n)

    def analyze_sentiment(self) -> Dict:
        pos_hits = sum(1 for w in self.words if w in POSITIVE_WORDS)
        neg_hits = sum(1 for w in self.words if w in NEGATIVE_WORDS)
        net_score = pos_hits - neg_hits

        if net_score > 0:
            classification = "Positive"
        elif net_score < 0:
            classification = "Negative"
        else:
            classification = "Neutral"

        return {
            "positive_count": pos_hits,
            "negative_count": neg_hits,
            "net_score": net_score,
            "sentiment": classification
        }

    def generate_report(self):
        print("\n" + "=" * 65)
        print("                 TEXT ANALYTICS REPORT")
        print("=" * 65)
        print(f"Total Characters (with spaces)   : {self.character_count(False)}")
        print(f"Total Characters (no spaces)     : {self.character_count(True)}")
        print(f"Total Word Count                 : {self.word_count()}")
        print(f"Sentence Count                   : {self.sentence_count()}")
        print(f"Average Word Length              : {self.average_word_length():.2f} characters")
        print(f"Vocabulary Diversity (TTR)       : {self.vocabulary_richness():.2%}")

        print("\nTop Informative Keywords (Filtered Stop Words):")
        for rank, (word, freq) in enumerate(self.top_keywords(5), start=1):
            print(f"  {rank}. '{word}': {freq} occurrences")

        senti = self.analyze_sentiment()
        print(f"\nHeuristic Sentiment Assessment:")
        print(f"  Tone Classification            : {senti['sentiment']} (Net score: {senti['net_score']})")
        print(f"  Positive Lexicon Matches       : {senti['positive_count']}")
        print(f"  Negative Lexicon Matches       : {senti['negative_count']}")
        print("=" * 65)


def run_demo():
    sample_text = """
    Artificial Intelligence is transforming modern industries with extraordinary and innovative solutions.
    Machine Learning algorithms extract valuable patterns from massive data, delivering fantastic efficiency.
    While ethical considerations pose a critical challenge and potential risk, the overall progress in deep learning
    remains promising, powerful, and deeply impactful.
    """
    print("=" * 60)
    print(" SAMPLE INPUT TEXT:")
    print("=" * 60)
    print(sample_text.strip())

    analyzer = TextAnalyzer(sample_text)
    analyzer.generate_report()


if __name__ == "__main__":
    if "--demo" in sys.argv or not sys.stdin.isatty():
        run_demo()
    else:
        print("Enter or paste your text to analyze (Press Ctrl+D or Ctrl+Z on new line when done):")
        user_input = sys.stdin.read()
        if user_input.strip():
            analyzer = TextAnalyzer(user_input)
            analyzer.generate_report()
        else:
            print("No text provided. Running demo instead.")
            run_demo()
