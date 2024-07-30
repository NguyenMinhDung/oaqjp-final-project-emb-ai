from emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        predicted_emotion = emotion_detector("I am glad this happened")
        self.assertEqual(predicted_emotion['dominant_emotion'], "joy")

    def test_anger(self):
        predicted_emotion = emotion_detector("I am really mad about this")
        self.assertEqual(predicted_emotion['dominant_emotion'], "anger")

    def test_disgust(self):
        predicted_emotion = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(predicted_emotion['dominant_emotion'], "disgust")

    def test_sadness(self):
        predicted_emotion = emotion_detector("I am so sad about this")
        self.assertEqual(predicted_emotion['dominant_emotion'], "sadness")

    def test_fear(self):
        predicted_emotion = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(predicted_emotion['dominant_emotion'], "fear")


if __name__ == '__main__':
    unittest.main()