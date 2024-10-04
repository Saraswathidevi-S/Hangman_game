hangman_stages = [
    # Final state: head, torso, both arms, and both legs
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    """,
    # Head, torso, both arms, and one leg
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / 
       |
    --------
    """,
    # Head, torso, and both arms
    """
       ------
       |    |
       |    O
       |   /|\\
       |   
       |
    --------
    """,
    # Head, torso, and one arm
    """
       ------
       |    |
       |    O
       |   /|
       |   
       |
    --------
    """,
    # Head and torso
    """
       ------
       |    |
       |    O
       |    |
       |   
       |
    --------
    """,
    # Head
    """
       ------
       |    |
       |    O
       |    
       |   
       |
    --------
    """,
    # Initial state: empty scaffold
    """
       ------
       |    |
       |    
       |    
       |   
       |
    --------
    """
]
