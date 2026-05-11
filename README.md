# Scale Up Series: Password Security Demo

[Pierre Olivier](https://sites.google.com/view/pierreolivier)

These instructions are there to help you reproduce at home the password cracking examples presented during the University of Manchester's scale up password security demo.
You can check out the slides used during that event here.

> ⚠️ Ethical Use Disclaimer
> 
> Although this demo introduces techniques that are commonly associated with offensive security, their purpose in this context is purely educational. Our goal is to help you understand how attackers operate, so you can build stronger, more secure systems.
> You are expected to use the knowledge and skills from this demo responsibly and ethically. Any use of these techniques outside of authorised, educational, or professional penetration testing contexts is strictly prohibited and may be illegal.

## Prerequisite

To reproduce the demo on various flavours of Windows, Mac, and Linux OSes, we will use a container: a virtual environment that can emulate a Linux machine on any modern computer, independently of the operating system it runs.
To that aim you will need to install the Docker container engine.
Follow these instructions based on your system:

- [Mac](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
- [Linux](https://docs.docker.com/desktop/setup/install/linux/)

To confirm the success of the installation, open a terminal (powershell on Windows) and run the `docker` command, you should see the following output:

```
docker

Usage:  docker [OPTIONS] COMMAND

A self-sufficient runtime for containers

Common Commands:
# ... more information about the docker command line usage follows ...
```

## Launching the Container

Run the container with the following command:

```bash
docker run -it olivierpierre/scale-up-password-demo
```

You will get access to a Linux-like command line environment preinstalled with all the software necessary to run the demos.

## Demo 1: Cracking a Simple Password

### Defining and Hashing a Weak Password

In this first demo we define a password, hash it with the MD5 hash function, then revert this hash to the original plain text password using `hashcat`.
Decide on a simple password and hash it with the following command:

```
echo -n "weakpw" | md5sum | cut -d " " -f 1 > hashed_pw.txt
```

Replace `weakpw` with the password of your choice.
For the sake of the exercise the password should be weak: its length should not be too long, and it should not be made of a wide variety of character: this ensures that the cracking process will complete in a reasonable amount of time.
A password made of 6 lower case letter characters should do.

After the above-mentioned command runs, the hash will be placed in a file named `hashed_pw.txt`, located in the working directory.
You can check out the hash by printing the content of this file on the console:

```
cat hashed_pw.txt 
171e6599c861cdbf291ad70e4ecdbc47
```

You will see a different hash if you chose a different password.

### Cracking the Hash

We can attempt to revert the hash into the plain text password with a brute force attack using `hashcat`.
To that aim run the following command:

```
hashcat -m 0 -a 3 hashed_pw.txt
```

Here `-m 0` means that `hashcat` will use the MD5 hash function, and `-a 3` indicates we want to attempt a brute force attack, i.e., trying all possible combinations of characters.
`hashcat` will initialise and start to run.
Things may take a variable amount of time based on the processing power of your computer and the length/complexity of the password you defined.
Once `hashcat` outputs the following line, the password has been cracked:

```
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
```

If you scroll up you should see the cracked password and its hash:

```
171e6599c861cdbf291ad70e4ecdbc47:weakpw
```

If the process takes too long, e.g., because the password you chose was too long/complex, you can hit <kbd>ctrl</kbd>+<kbd>c</kbd> to stop `hashcat` and repeat the previous steps to set a password that is faster to crack.

## Demo 2: Cracking Rockyou.txt

[RockYou.txt](https://github.com/josuamarcelc/common-password-list/blob/main/README.md) is a real-world collection of millions of passwords that were exposed after the [2009 breach of the RockYou service](https://en.wikipedia.org/wiki/RockYou#Data_breach). 
It is commonly used in cybersecurity for password cracking, penetration testing, and research on weak password patterns and user authentication security.

A total of 14M passwords were leaked in plain text through that breach.
For the sake of the exercise a subset of 1.4M password has been hashed with MD5, to emulate a situation in which a hacker would have stolen encrypted (hashed) password from a modern website/application.
The list of hashes is present in the container's local working directory in a file named `rockyou_md5.txt`.
You can display the hashes with the following command:

```
cat rockyou_md5.txt
d6ee950cebbf40c4659fa25868c746dc
f497abcefc3a227afbf438f03864d51c
bfbf2f5c962d4fd32858961dd569755c
8cdfffeb647bdd1edc97679d49d63de3
2a9d2cf8ee0b1b339c61f441825a1113
3361496b3e2758bbd2a80bc749026146
8d5a4765610178afdebb28811985730b
c114627ba769b3edf6d5a5ba1a2fca3d
# ... more hashes follow ...
```

Displaying the entire 1.5M hashes would take quite some time, you can hit <kbd>ctrl</kbd>+<kbd>c</kbd> to stop the process.

We can call `hashcat` on that list of hashes to revert as many hashes as possible back to the plain text passwords 

```
hashcat -m 0 -a 3 rockyou_md5.txt
```

`hashcat` will start to run and will display the password for each hash successfully cracked.
Rockyou.txt contains tons of weak password, and you should quickly see thousands of passwords:

```
783240a5bd72ca8b369ef0ebeceef0d7:physhi1                  
42240af83ff072c882917685469d793b:284843m                  
c0959cddd7e5c94df36d932ee59d2f65:sccihak                  
127aa7962e0701419e2c2b904e6526b2:cbotti1                  
670a2d975f682ae2b791ea295d0b469a:dhymalk                  
6ab163544b461d4c030bd515584e2e41:azncrew                  
3c834814e76b114488390275cf83777b:1myshop                  
7e18c6786acff9960abfc76001fc4e3c:004803m                  
4769651a082a39126f3703a917bf4d9a:hgisti1                  
c6ab4b4aaf38cf33783dc2d8556f0972:jbontop                  
fe0d14fc66d6e54bc4484d1f3f28f5f9:4969vbh                  
b43123e637eb5e22199fe2b19eeeb68b:ubokai1                  
a583b6db156e7f27fe88da15675a7172:r159ctc                  
d4900b12a7b68fb4682a94175f333969:396917c                  
1a4a0ec3fffa26cd8e2aab6c080fa0a8:aznxtc2                  
b9a9652753ed75409dde7101d0f83c32:fgicrew                  
```

> ⚠️ These are real world passwords set by real people, and some of these passwords do contain foul language

As the process run you can hit the <kbd>p</kbd> key to pause the process and check `hashcat`'s status with <kbd>s</kbd>.
Among other information, you can see the amount of passwords recovered over the total amount of hashes to process:

```
Recovered........: 368506/1494463
```

The speed in hashes tried per second:

```
Speed.#1.........:   519.1 MH/s (8.70ms)
```

Or the number of hashes remaining to recover:

```
Remaining........: 1122475 (75.11%)
```

To unpause `hashcat` hit the <kbd>r</kbd> key.
Recovering the entirety of the passwords would take an extremely long time, to top the process hit <kbd>ctrl</kbd>+<kbd>c</kbd>.
