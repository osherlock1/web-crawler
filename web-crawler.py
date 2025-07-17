from storage import initiate_db
from cli_config import cli_args





if __name__ == '__main__':

    args = cli_args()
    initiate_db(args.db)
    print(args.seed)