for i in range(2, 21):
    with open(f"tables/multiplication_table_of_{i}", "w") as f:
        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}\n") 