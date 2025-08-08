from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        # T5: Joy result
        tc_1 = emotion_detector('I am glad this happened')
        self.assertEqual(tc_1['dominant_emotion'], 'joy')
        # T5: Anger result
        tc_2 = emotion_detector('I am really mad about this')
        self.assertEqual(tc_2['dominant_emotion'], 'anger')
        # T5: Disgust result
        tc_3 = emotion_detector('I feel disgusted just hearing about it')
        self.assertEqual(tc_3['dominant_emotion'], 'disgust')
        # T5: Sadness result
        tc_4 = emotion_detector('I am so sad about this')
        self.assertEqual(tc_4['dominant_emotion'], 'sadness')
        # T5: Fear result
        tc_5 = emotion_detector('I am very afraid this will happen')
        self.assertEqual(tc_5['dominant_emotion'], 'fear')

unittest.main()