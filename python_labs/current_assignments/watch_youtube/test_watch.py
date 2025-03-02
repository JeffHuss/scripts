import pytest
from watch import parse

def test_valid_youtube_embeds():
    # Test regular http YouTube embed
    assert parse('<iframe src="http://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    
    # Test https YouTube embed
    assert parse('<iframe src="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    
    # Test with www prefix
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    
    # Test with additional iframe attributes
    assert parse('<iframe width="560" height="315" src="https://youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    
    # Test with URL parameters
    assert parse('<iframe src="https://www.youtube.com/embed/xvFZjo5PgG0?autoplay=1"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    
    # Test with different video ID containing hyphens and underscores
    assert parse('<iframe src="https://youtube.com/embed/dQw4w9WgXcQ"></iframe>') == "https://youtu.be/dQw4w9WgXcQ"

def test_invalid_inputs():
    # Test with non-YouTube URL
    assert parse('<iframe src="https://vimeo.com/123456"></iframe>') is None
    
    # Test with malformed iframe
    assert parse('<iframe href="https://youtube.com/embed/xvFZjo5PgG0"></iframe>') is None
    
    # Test with no iframe
    assert parse('Check out this video: https://youtube.com/watch?v=xvFZjo5PgG0') is None
    
    # Test with empty string
    assert parse('') is None