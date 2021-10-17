import spacy

from typing import NamedTuple
from itertools import product


nlp = spacy.load("en_core_web_md")


class Match(NamedTuple):
    sentence: str = ""
    similarity: float = 0
    document: str = ""


class Sentence(object):
    def __init__(self, spacy_sent):
        self.spacy_sent = spacy_sent

        # Every value here should be a list of Match objects
        self.suspects = []

    def add_suspect(self, match):
        self.suspects.append(match)

    @property
    def has_suspects(self):
        return bool(self.suspects)

    @property
    def as_json(self):
        return {
            "sentence": self.spacy_sent.text,
            "suspects": [
                dict(match._asdict()) for match in self.suspects
            ]
        }


class TargetDocument(object):
    def __init__(self, document_name, document_text):
        self.name = document_name
        self.doc = nlp(document_text or "")


class DocumentComparer(object):

    SIMILARITY_THRESHOLD = 0.95

    def __init__(self, original):
        self.doc = original.doc
        self.sentences = [Sentence(sent) for sent in self.doc.sents if DocumentComparer._filter_sentence(sent)]

    def compare_to(self, target_doc):
        for sentence, match in self._similar_sentences(target_doc):
            sentence.add_suspect(match)

    @property
    def as_json(self):
        return [sentence.as_json for sentence in self.sentences if sentence.has_suspects]

    def _similar_sentences(self, document: TargetDocument):
        document_sentences = [sent for sent in document.doc.sents if DocumentComparer._filter_sentence(sent)]

        for original_sent, document_sent in product(self.sentences, document_sentences):
            similarity = original_sent.spacy_sent.similarity(document_sent)

            if similarity >= DocumentComparer.SIMILARITY_THRESHOLD:
                yield original_sent, Match(
                    sentence=document_sent.text,
                    similarity=similarity,
                    document=document.name
                )

    @staticmethod
    def _filter_sentence(sent):
        return bool(sent.text.strip())