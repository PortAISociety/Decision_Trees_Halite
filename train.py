#!/usr/bin/env python3

import model


def main():
    m = model.HaliteModel()
    m.train_on_folder("./training")
    m.save(file_name="out/dt.svc")
    print("Training complete. SVC file at out/dt.svc")
    print("call ./run_game.sh to test bot")

if __name__ == "__main__":
    main()
