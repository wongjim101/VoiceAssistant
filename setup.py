from setuptools import setup, find_packages

setup(name='VoiceAssistant', 
    version='1.0', 
    packages=find_packages(),
    install_requires=[
        'PyAudio',
        'SpeechRecognition'
    ])