"use strict"; 

const worker = require("streaming-worker");
const path = require("path");

function Netlink(options) {
    const addon_path = path.join(__dirname, "build/Release/netlink_worker");
    return worker(addon_path, options);
}

module.exports = {Netlink};
