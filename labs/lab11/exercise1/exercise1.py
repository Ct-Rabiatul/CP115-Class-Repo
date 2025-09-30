num_rounds = int(input())
rounds_processed = 0
final_score = 0
# TODO: Your code here
# Use input() inside the loop to get each round's score
for num_rounds in range (num_rounds) :
    round_score = float(input())
    
    if round_score > 100:
       round_score *= 1.2
    
    final_score += round_score
    rounds_processed += 1



print(f"{final_score:.1f}")
print(rounds_processed)