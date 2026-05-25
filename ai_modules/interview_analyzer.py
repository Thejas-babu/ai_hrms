def analyze_interview(answer):

    score = len(answer) / 10

    return {
        "confidence_score": score,
        "communication_score": score + 5
    }
