const fetch = require("node-fetch");
const { program } = require('commander');
const fs = require('fs');
const unzipper = require('unzipper');
program.option('--url <url>', 'url of the pwa');
program.option('--archive <archive>', 'name of the archive');
program.parse(process.argv);

const appurl = program.url;
const appname = program.archive;

async function main() {
    var manifest = await (await fetch(`https://pwabuilder-api-prod.azurewebsites.net/manifests`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            siteUrl: appurl
        })
    })).json();
    var id = manifest.id;
    var response = await (await fetch(
        `https://pwabuilder-api-prod.azurewebsites.net/manifests/${id}/build?ids=1&href=${appurl}`,
        {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                platforms: ["windows10"],
                dirSuffix: "windows10",
                parameters: []
            })
        },
    )).json();
    console.log(response);
    var archive = response.archive;
    (await fetch(archive)).body.pipe(unzipper.Extract({ path: appname }));
}

main();