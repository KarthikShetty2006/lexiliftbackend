dummy_user = {
  "name": "Aarav",
  "age": 9,
  "guardianEmail": "parent@example.com"
}

dummy_assessment = {
  "userId": "123",
  "type": "initial",
  "scores": {"phonological": 0.7, "surface": 0.8},
  "derived": {"subtypes": ["Phonological"], "severity": {"Phonological": "mid"}}
}

dummy_exercise = {
  "userId": "123",
  "mode": "read-aloud",
  "items": [{"text": "bridge"}, {"text": "dog"}]
}

dummy_drill = {
  "userId": "123",
  "type": "minimal_pairs",
  "payload": {"pairs": [["bid","did"],["pad","bad"]]}
}
