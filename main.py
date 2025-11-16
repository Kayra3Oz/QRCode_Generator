import Generator
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--url", type=str, required=True)

    args = parser.parse_args()

    generator = Generator.Generator(args.url)
    generator.generate()
