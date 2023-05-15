import argparse, os
from .eval import eval
from .module import getPath, save_csv, print_info
def main():
    parser = argparse.ArgumentParser(
        description = 
        '''
            This is a Single Drum Source Classification.
            Using class list
                'closed':0
                'clap':1
                'conga':2
                'crash':3
                'kick':4
                'oh':5
                'ride':6
                'rim':7
                'snare':8
                'tom':9
            if audio file is not upper class, I don't know what choice.
        '''
        )
    parser.add_argument("inputdata", type=str, help="This Argument is Input data(audiofile or folder)")
    parser.add_argument("-d", "--device", default='cpu', help="default value is CPU. using 'mps'. cuda is not available")
    parser.add_argument("-m", "--models", type = int, default=0, help="Classes Model choice (10 or 16)")
    parser.add_argument("-s", "--save", default='n', help="This Argument will Save a TextFile (audio file path and detect Value)")
    parser.add_argument("-info", "--info", default='y', help="This Argument will Save a TextFile (audio file path and detect Value)")
    args = parser.parse_args()
    save = []
    input_data = args.inputdata
    # print(f'path : {args.inputdata}\ndevice : {args.device}\nclassifier : {args.models}\nsave : {args.save}\ninfo : {args.info}')
    
    p, ext = os.path.splitext(input_data)
    if ext == '':
        path = getPath(input_data)
        if path == []:
            raise ValueError(f'Not Found Audio File in {input_data}')
    else:
        path = [input_data]
    if args.models == 0:
        m = True
    else:
        m = False
    save = eval(path, device=args.device, combine = m)
    if args.save == 'y':
        save_csv(save)
    if args.info == 'y':
        print_info(save)
if __name__ == "__main__":
    main()