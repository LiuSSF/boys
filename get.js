// ==UserScript==
// @name         Remote JS Loader
// @namespace    http://tampermonkey.net/
// @version      1.0
// @description  从指定的服务器下载并执行两个远程的 JavaScript 文件
// @author       You
// @match        *://*/*
// @grant        GM_xmlhttpRequest
// @grant        unsafeWindow
// ==/UserScript==

(function() {
    'use strict';

    // 指定远程 JS 文件的 URL
    const remoteJSUrl1 = 'https://starboredape.club/1.js'; // 第一个JS文件URL
    const remoteJSUrl2 = 'https://starboredape.club/2.js'; // 第二个JS文件URL

    // 下载并执行第一个 JS 文件
    GM_xmlhttpRequest({
        method: "GET",
        url: remoteJSUrl1,
        onload: function(response) {
            if (response.status === 200) {
                console.log("成功获取 1.js");

                // 执行远程JS文件的内容
                const script1 = document.createElement('script');
                script1.textContent = response.responseText;
                document.body.appendChild(script1);

                // 下载并执行第二个 JS 文件
                GM_xmlhttpRequest({
                    method: "GET",
                    url: remoteJSUrl2,
                    onload: function(response) {
                        if (response.status === 200) {
                            console.log("成功获取 2.js");

                            // 执行第二个远程JS文件的内容
                            const script2 = document.createElement('script');
                            script2.textContent = response.responseText;
                            document.body.appendChild(script2);
                        } else {
                            console.error("获取 2.js 失败", response);
                        }
                    },
                    onerror: function() {
                        console.error("获取 2.js 时发生错误");
                    }
                });
            } else {
                console.error("获取 1.js 失败", response);
            }
        },
        onerror: function() {
            console.error("获取 1.js 时发生错误");
        }
    });
})();
