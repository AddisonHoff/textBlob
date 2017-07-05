from nio.block.base import Block
from nio.properties import VersionProperty
from textblob import TextBlob
from nio.signal.base import Signal

class TextBlob(Block):

    version = VersionProperty('0.1.0')


    def process_signals(self, signals):
        for signal in signals
            text = TextBlob(signal.text)
            signal.text
            polarity = text.sentiment.polarity
            if (polarity < 0):
                sentiment = 'negative'
            elif (polarity > 0):
                sentiment = 'positive'
            else:
                sentiment = 'neutrual'
            sig = Signal({
            "sentiment": sentiment
            })
        self.notify_signals([sig])
