// ==UserScript==
// @name         Remote JS Loader (No Cache)
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  从指定服务器下载并执行两个远程的 JavaScript 文件，强制更新到最新版本
// @author       You
// @match        *://*/*
// @grant        GM_xmlhttpRequest
// @grant        unsafeWindow
// ==/UserScript==

(function() {
    'use strict';

    // 定义远程 JS 文件的 URL
    const remoteJSUrl1 = 'https://starboredape.club/1.js'; // 第一个JS文件URL
    const remoteJSUrl2 = 'https://starboredape.club/2.js'; // 第二个JS文件URL

    // 下载并执行第一个 JS 文件
    GM_xmlhttpRequest({
        method: "GET",
        url: remoteJSUrl1,
        headers: {
            "Cache-Control": "no-cache", // 强制跳过缓存
            "Pragma": "no-cache"        // 兼容性头部，确保无缓存
        },
        onload: function(response) {
            if (response.status === 200) {
                console.log("成功获取 1.js，开始执行");
                const script1 = document.createElement('script');
                script1.textContent = response.responseText;
                document.head.appendChild(script1);

                // 下载并执行第二个 JS 文件
                GM_xmlhttpRequest({
                    method: "GET",
                    url: remoteJSUrl2,
                    headers: {
                        "Cache-Control": "no-cache", // 强制跳过缓存
                        "Pragma": "no-cache"        // 兼容性头部，确保无缓存
                    },
                    onload: function(response) {
                        if (response.status === 200) {
                            console.log("成功获取 2.js，开始执行");
                            const script2 = document.createElement('script');
                            script2.textContent = response.responseText;
                            document.head.appendChild(script2);
                        } else {
                            console.error("获取 2.js 失败，状态码:", response.status);
                        }
                    },
                    onerror: function() {
                        console.error("获取 2.js 时发生错误");
                    }
                });
            } else {
                console.error("获取 1.js 失败，状态码:", response.status);
            }
        },
        onerror: function() {
            console.error("获取 1.js 时发生错误");
        }
    });
})();
