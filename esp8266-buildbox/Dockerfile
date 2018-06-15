FROM ubuntu:14.04
MAINTAINER chipolux <nakyle.wright@gmail.com>

RUN apt-get update && apt-get install -y \
    autoconf \
    automake \
    bison \
    flex \
    g++ \
    gawk \
    gcc \
    git \
    gperf \
    libexpat-dev \
    libtool \
    make \
    ncurses-dev \
    python-dev \
    python-pip \
    sed \
    texinfo \
    tmux \
    unzip \
    vim \
    wget \
    zsh
RUN pip install git+https://github.com/themadinventor/esptool.git

RUN useradd -s /bin/zsh -m esp8266 && \
    echo "esp8266 ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/esp8266 && \
    chmod 0440 /etc/sudoers.d/esp8266

USER esp8266
ENV HOME=/home/esp8266

WORKDIR $HOME
RUN git clone https://github.com/pfalcon/esp-open-sdk.git --recursive
WORKDIR esp-open-sdk
RUN make STANDALONE=n
ENV PATH=$PATH:$HOME/esp-open-sdk/xtensa-lx106-elf/bin
ENV ESP_OPEN_SDK=$HOME/esp-open-sdk
ENV CPATH=$ESP_OPEN_SDK/sdk/include
ENV LD_LIBRARY_PATH=$ESP_OPEN_SDK/sdk/lib

WORKDIR $HOME
RUN git clone https://github.com/tommie/esptool-ck.git
WORKDIR esptool-ck
RUN make
ENV PATH=$PATH:$HOME/esptool-ck

WORKDIR $HOME
RUN git clone https://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh
RUN cp $HOME/.oh-my-zsh/templates/zshrc.zsh-template $HOME/.zshrc
RUN sed -i 's/robbyrussell/steeef/g' $HOME/.zshrc && \
    echo "setopt no_nomatch" >> $HOME/.zshrc

RUN mkdir $HOME/project
WORKDIR $HOME/project
ENTRYPOINT /bin/zsh
