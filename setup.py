import setuptools

with open("README.md", 'r+') as f:
    print("opened")
    long_de = f.read()


setuptools.setup(
    name="spotidnldr", # Replace with your own username
    version="1.0.0",
    author="Rohit Patil",
    author_email="rahulhimesh09@gmail.com",
    description="the spotify song downloader",
    long_description = long_de,
    long_description_content_type="text/markdown",
    url="https://github.com/raprocks/spotindnldr",
    packages=["spotidnldr",],
    install_requires=[
        "spotipy",
        "youtube-dl",
        "eyeD3",
        "requests",
        "click",
        "ffmpeg-python",
        "ytmusicapi",
    ],
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "License :: GPL-3.0-or-later",
        "Operating System :: OS Independent",
    ],
    entry_points='''
        [console_scripts]
        spoti=spotidnldr.clifi:download
    ''',
    python_requires='>=3.8',
    include_package_data=True,
)