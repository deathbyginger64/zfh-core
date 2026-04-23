from data.dataset_generator import DatasetGenerator

def main():
    generator = DatasetGenerator(num_samples=100)
    generator.generate()

if __name__ == "__main__":
    main()