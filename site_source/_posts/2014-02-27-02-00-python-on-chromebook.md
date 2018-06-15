---
layout: post.html
title: Working In Python From A Chromebook
---

Several weeks ago someone posted on [/r/python][1] about programming in Python
on a Chromebook. I've been doing precisely that for some time now and thought
I'd put my thoughts into a more consumable form.

A Chromebook can be a great device, but only if it fits your needs.
Unfortunately it's been judged only suitable for folks like bloggers, writers,
and social media types who can live entirely in "the cloud". I'd like to
challenge that notion!

Now, I won't beat around the bush, most of this is advice that's the same as
if you were simply working on a remote Linux server since that's essentially
the best way to do it that I've found, but there are a few tips and tricks to
make that easier on a chromebook.

Here are a few major points I think you should consider before you make the
decision to use a chromebook.

* Are you fine with working almost exclusively from a console?
* Do the things you develop mostly interact via console or a web type interface?
* Is there internet readily available just about everywhere you want to work?
* Or are you fine with the cost of buying a 3G or LTE compatible chromebook
and the cost of the plan?
* Are you comfortable with dual-booting and with Linux style environments?

If you answered yes to most of those questions then a chromebook could probably
fit your needs well!

Another big thing for me is the cost of a chromebook, I honestly wouldn't
recommend spending more than $300 USD on one unless you're pitching in for the
cell card as it is simply not a device that's powerful enough to weigh so
heavily on the wallet. I personally use a C7 series Acer chromebook I picked up
for a little over $200 USD and it has fit my work style perfectly and is easily
replaceable if I break or lose it.

##Chrome OS Toolbox

So, you'll be doing pretty much everything from a console when you're booted up
into Chrome OS. There are plenty of web-based 'compiler' and 'executor' style
sites that will run an arbitrary bit of Python for you, but they're still
relatively young and limited right now.

You'll want to grab a few extensions:

* [Secure Shell][2] - the de-facto SSH client for Chrome OS.
* [Text][3] - a local plain text editor, simple and sweet.
* [Chrome Remote Desktop][4] - an RDP client, works for connecting to most
stuff that can run chrome provided you install and allow the app on that PC.

Also, if you don't have a remote Linux machine you can SSH to then half of
this won't be much use to you. I highly recommend picking up a cheap virtual
server from [Digital Ocean][5] as I use them extensively and they have great
service for the price. A simple $5 a month Ubuntu VPS can be super handy!

If you plan on buying you can use my [referral link][6] if you want.
But there are lots of VPS hosts out there like [Rackspace][7], and
[Amazon's VPS offerings][8]. There are entire sites devoted to who you should
go with and how to configure a VPS so I'm leaving that bit to you as no
solution is best for everyone.

##Working On A Server

While you're booted into Chrome OS there's not much you can do locally.
This is a great opportunity to learn about working on remote servers when all
you have is shell access! I'm assuming from here on that you have a remote
Linux server up and running that you can SSH to, if that's not the case go
ahead and skip down to the *Working Locally* section.

Using Secure Shell is super easy! Just open it up and it defaults to filling
out a new connection. Just type in the name in the big top field, and then the
user and server in the two fields immediately below, the rest is all optional.
You'll need to do extra configuration if you want to use key pairs and such but
straightforward password authentication is fine for most folks. You can see a
screenshot below.

<img src="http://i.imgur.com/hz9QNAE.png?1" alt="Secure Shell Screenshot">

Then just connect on up! You can save your connection if you like, it'll sync
your saved connections and all your settings between all your chrome
instances, provided they're linked to the same Google account and you have
syncing enabled.

Once connected to your server you'll want to install a few things:

* [tmux][9] - a terminal multiplexer. (*The* terminal multiplexer.)
* [IPython][10] - when you're working from a console full time, IPython is a
huge help.
* And your text-mode editor of choice, be that [Emacs][11], [Vim][12] or even
just [nano][13] if you're new to console based editing.

For the sake of this walk through I'm going to use nano as it's really easy
to pick up for beginners. Feel free to replace any mention of it with your
editor of choice!

###Using tmux

This can be a bit a bit foreign to most people, but it will drastically change
your work flow once you get used to it. There are tons of great tutorials and
getting started guides for tmux so I'm just going to go over the basics.

To start just run `tmux` in your console, this will start up a new tmux session
and drop you into it. By default the new session just has a single window with
one pane that will start your default shell.

When you're in a tmux session you have a new layer of keyboard shortcuts
available to you, you can access them by hitting `Ctrl+B`, this puts you into a
special input mode and your next key press won't have the same consequences as
usual.

The basic commands you'll use the most are:

* `Ctrl+B C` - Creates a new window.
* `Ctrl+B N` - Switches to the *next* window.
* `Ctrl+B P` - Switches to the *previous* window.
* `Ctrl+B %` - Creates a new pane, splitting the current pane vertically.
* `Ctrl+B "` - Creates a new pane, splitting the current pane horizontally.
* `Ctrl+B O` - Cycles between panes in the active window.
* `Ctrl+B Q` - Shows the numbers of the panes in the current window.
* `Ctrl+B D` - Detaches from the current tmux *session*.

My usual process is to have a pane open with a script I'm working on, and two
smaller panes open below it, one for a shell and another for an IPython
instance. To do that you can use `Ctrl+B "` to split your window horizontally,
then `Ctrl+B O` to cycle until you're in the bottom pane, then `Ctrl+B %` to
split the bottom pane vertically. You can also do `Ctrl+B Esc` and then a
directional key to shift the closest pane border in that direction, you can
see what my screen looks like [here][14].

A few tips, instead of using `Ctrl+B O` to cycle through panes you can hit
`Ctrl+B Q` to display numbers over each pane then quickly press the number of
the pane you want to select and it will move you there. You can also detach
from your tmux session to go back to the raw shell by pressing `Ctrl+B D`,
this leaves the session running in the background and you can re-attach to it
later by running `tmux attach [session name]`, note that session name is
optional if you only have one tmux session running. Use `tmux list-session`
to see a list of all active sessions and their names.

There are also a lot of tmux commands for things like pasting, scrolling the
buffer, and such. You can find most of that [in the docs][15].

###Using nano

Nano is a very simple console text editor available on most flavors of Linux.
It's a great tool for beginners as it is simple to configure and use.
Eventually it would be recommended to move on to a more full featured editor
like Vim or Emacs, but it's all about your comfort level so go with what suits
you best.

First off I always configure nano with an alias to set some stuff up the way I
like it: `alias nano="nano -w -i -T 4 -E"`

This tells nano to start with no line wrap `-w`, auto indent `-i`, tabs are
four spaces `-T 4`, and tabs should be replaced by spaces `-E`. This fits
with PEP 8 and the line wrap helps me be wary of lines that grow longer than
79 characters.

You will also want to get some proper syntax highlighting set up. You can find
a ton of great syntax highlighting files [here][16]!

To set those up just download them, then I like to copy them into a `~/.nano/`
directory and then reference the ones I need in my `~/.nanorc` file using
statements like `include "~/.nano/python.nanorc"`.

That covers most of your bases for working from a console, you can edit your
scripts in nano in one pane and quickly swap to other panes to commit changes,
execute the script, or test out some syntax in IPython with it's awesome
tab-completion and help functions.

It can be a bit painful at first, especially if you're not all that familiar
with Linux, but once you get the hang of it I promise it feels very empowering
as you'll know that you can perform great work even if all you've got is a
terminal!

##Working Locally

Working locally on a chromebook is a more involved process that's tough to
cover. It relies on configuring your chromebook to dual-boot to some flavor
of Linux and then setting up your preferred environment there. It's really
only necessary if you need to work on some GUI based stuff, really prefer a
GUI to work in, or don't have internet access and can't reach out to your
server.

You can also use things like [Crouton][17] to run a Linux instance in parallel
to Chrome OS, I favor partitioning and dual-booting but that's simply out of
familiarity. You can find a guide to setting up Crouton [here][18] and one for
dual-booting [here][19].

Once you've got into a Linux environment on your chromebook it's as simple as
setting up your normal development environment just like usual. For those who
don't often develop from Linux, I prefer to keep things light by using Xubuntu
and I use [Spyder2][20] as my IDE of choice as it is very light and has
excellent tab-completion, syntax highlighting, and debugging features.

I know many people are concerned with how tight the resources are on a
chromebook but I've ran into very few issues when working both in Chrome OS and
when booted into Xubuntu though your mileage may vary.

##Final Thoughts

In the end, a chromebook certainly isn't the right choice for everyone and it's
up to you to determine if it's worth the relatively minor investment.
Personally I've had a lot of use out of mine and I'd recommend it if you're just
looking for a really lightweight portable and you can utilize heavier machinery
over the network.

I also didn't really touch on the RDP stuff, Google's app page explains how to
use it better than I can and it is very useful if you'd like to just jump over
onto a home Windows or Mac workstation to do some work but I'd recommend using
SSH when possible as RDP connections are notoriously laggy and can get
frustrating.

I hope this quick run through of how I use my chromebook has helped you in some
way and if you have some advice you'd like to add feel free to drop a comment
below! Also if it's any help this entire site was made pretty much entirely
using just this chromebook I'm on right now! Thanks for reading!

[1]: http://www.reddit.com/r/python
[2]: https://chrome.google.com/webstore/detail/secure-shell/pnhechapfaindjhompbnflcldabbghjo
[3]: https://chrome.google.com/webstore/detail/text/mmfbcljfglbokpmkimbfghdkjmjhdgbg
[4]: https://chrome.google.com/webstore/detail/chrome-remote-desktop/gbchcmhmhahfdphkhkmpfmihenigjmpp
[5]: https://www.digitalocean.com/pricing
[6]: https://www.digitalocean.com/?refcode=f9b2ce354d85
[7]: http://www.rackspace.com/cloud/vps/
[8]: http://aws.amazon.com/vpc/
[9]: http://tmux.sourceforge.net/
[10]: http://ipython.org/
[11]: http://www.gnu.org/software/emacs/
[12]: http://www.vim.org/
[13]: http://www.nano-editor.org/
[14]: http://i.imgur.com/TGQRHB6.png
[15]: http://www.openbsd.org/cgi-bin/man.cgi?query=tmux&sektion=1
[16]: https://github.com/scopatz/nanorc
[17]: https://github.com/dnschneid/crouton
[18]: http://lifehacker.com/how-to-install-linux-on-a-chromebook-and-unlock-its-ful-509039343
[19]: http://chromeos-cr48.blogspot.com/2013/10/chrubuntu-for-new-chromebooks-now-with.html
[20]: https://code.google.com/p/spyderlib/
