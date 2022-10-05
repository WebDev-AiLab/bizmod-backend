# base image
FROM node:16

# set working directory
WORKDIR /usr/src/app

# add /usr/src/app/node_modules/.bin to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH


# install and cache app dependencies
RUN npm install -g npm@8.19.2
COPY package.json /usr/src/app/package.json
RUN npm install --force
RUN npm install react-scripts@1.1.1 -g --silent


COPY . .

EXPOSE 3000