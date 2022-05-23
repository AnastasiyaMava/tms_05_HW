FROM ubuntu:focal

ENV MONGOCXX_VERSION=3.6.0

ENV TZ=Europe/Kiev
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone


RUN apt update && apt install  -y \
                     build-essential \
                     autoconf \
                     automake \
                     cmake \
                     curl \
                     gcc \
                     g++ \
                     git \
                     libtool \
                     make \
                     unzip \
                     wget \
                     python3 \
                     golang

RUN apt install -y libprotobuf-dev

RUN  apt install -y libcairo2-dev

RUN cd /opt && git clone -b v1.32.0 https://github.com/grpc/grpc \
    && cd grpc \
    && git submodule update --init --recursive \
    && mkdir -p cmake/build \
    && cd cmake/build \
    && cmake ../.. -DgRPC_INSTALL=ON -DBUILD_SHARED_LIBS=ON \
    && make -j 4 \
    && make install

RUN cd /opt && wget http://downloads.sourceforge.net/project/boost/boost/1.68.0/boost_1_68_0.tar.gz \
  && tar xfz boost_1_68_0.tar.gz \
  && rm boost_1_68_0.tar.gz \
  && cd boost_1_68_0 \
  && ./bootstrap.sh --prefix=/usr/local --with-libraries=program_options \
  && ./b2 install

RUN apt install -y libcurl4-openssl-dev

RUN apt install -y libconfig++-dev

RUN apt-get update 

RUN apt-get install -y google-mock

RUN apt-get install -y libgtest-dev

RUN cd /usr/src/googletest/googletest && mkdir build && cd build && cmake .. && make && cd lib && ls -la

RUN cp /usr/src/googletest/googletest/build/lib/libgtest* /usr/lib/

RUN mkdir /usr/local/lib/googletest

RUN ln -s /usr/lib/libgtest.a /usr/local/lib/googletest/libgtest.a

RUN ln -s /usr/lib/libgtest_main.a /usr/local/lib/googletest/libgtest_main.a

WORKDIR /opt

COPY . /opt/nesting_client_test

RUN cd /opt/nesting_client_test && mkdir build && cd build && cmake .. && make -j4  && cd app && ls

WORKDIR /opt/nesting_client_test/build/app

ENTRYPOINT ["./main ../../resources/nesting_request1706.json ../../resources/get_products.json 3 false"]
