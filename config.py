from os.path import join

root_folder = r"/home/tumpa/cai"
input_plain: str = join(root_folder, "plaintext.txt")
input_ocs: str = join(root_folder, "ocs.json")


regex = r"(\d+(?:\.\d+)?(?:K|M)?)\n(\d*)\n?(.+)\n\n(.+)\n\nby (.+)\n\n((?:.+\n?)*)"


del join
