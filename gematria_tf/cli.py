import argparse
from pathlib import Path

from .bhsa import fetch_source, load_source, source_directory
from .calculator import METHODS, TRANSFORMS
from .generator import generate
from .representations import READINGS


def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate pinned BHSA 2021 gematria add-on features")
    parser.add_argument("--fetch", action="store_true", help="Download BHSA through Text-Fabric into its standard data directory")
    parser.add_argument("--output", type=Path, default=Path("tf/2021"))
    parser.add_argument("--methods", nargs="+", choices=METHODS, default=list(METHODS))
    parser.add_argument("--transforms", nargs="+", choices=TRANSFORMS, default=["identity"])
    parser.add_argument("--readings", nargs="+", choices=READINGS, default=["ketiv"])
    parser.add_argument("--language", choices=["all", "hebrew"], default="all")
    parser.add_argument("--limit", type=int, help="First N selected word nodes; labelled partial in metadata")
    args = parser.parse_args(argv)
    try:
        source = fetch_source() if args.fetch else source_directory()
        api, lock = load_source(source)
        result = generate(api, source, lock, args.output, methods=args.methods,
                          transforms=args.transforms, readings=args.readings, language=args.language, limit=args.limit)
    except (ValueError, RuntimeError, OSError) as error:
        parser.exit(1, f"gematria-tf: {error}\n")
    print(f"Verified {len(result['features'])} features for {result['wordCount']:,} word nodes in {args.output}")


if __name__ == "__main__":
    main()
