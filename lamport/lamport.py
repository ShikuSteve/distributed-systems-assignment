
# 5 processes (P0 - P4)
processes = 5

# 10 messages as (sender, receiver)
messages = [
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 0),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 0),
    (4, 1)
]

# Initialize Lamport clocks
clocks = [0] * processes

# Record timestamps for each message
timestamps = []

def send_event(sender, receiver):
    global clocks, timestamps
    clocks[sender] += 1  # increment sender clock for send event
    send_time = clocks[sender]
    
    # Receiver updates clock on receive
    clocks[receiver] = max(clocks[receiver], send_time) + 1
    
    # Record event
    timestamps.append({
        'sender': sender,
        'receiver': receiver,
        'send_time': send_time,
        'receive_time': clocks[receiver]
    })

# Process all messages
for s, r in messages:
    send_event(s, r)

# Print results
print("Lamport timestamps for each message:")
for t in timestamps:
    print(f"P{t['sender']} -> P{t['receiver']}: send={t['send_time']}, receive={t['receive_time']}")

print("\nFinal clocks for each process:")
for i, c in enumerate(clocks):
    print(f"P{i}: {c}")
