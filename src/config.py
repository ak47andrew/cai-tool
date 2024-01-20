from os.path import join

ROOT_FOLDER = r"/home/tumpa/cai"
INPUT_PLAIN: str = join(ROOT_FOLDER, "plaintext.txt")
INPUT_OCS: str = join(ROOT_FOLDER, "ocs.json")


REGEX = r"(\d+(?:\.\d+)?(?:K|M)?)\n(\d*)\n?(.+)\n\n(.+)\n\nby (.+)\n\n((?:.+\n?)*)"


del join
