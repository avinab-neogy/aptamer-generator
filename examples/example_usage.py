from aptamer_generator import AptamerGenerator

def main():
    print("Aptamer Generation Demo\n-----------------------")  # Debug print
    
    generator = AptamerGenerator(seed=42)
    print("Generator initialized")  # Debug print
    
    # Generate candidates with relaxed GC range for testing
    candidates = generator.generate_candidates(
        num=5,
        length=40,
        gc_range=(0.0, 1.0)  # Test with all sequences accepted
    )
    print(f"Generated {len(candidates)} candidates\n")  # Debug print
    
    for i, seq in enumerate(candidates, 1):
        gc_percent = (seq.count('G') + seq.count('C')) / len(seq) * 100
        print(f"Sequence {i}: {seq} (GC: {gc_percent:.1f}%)")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
