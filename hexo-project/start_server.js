const Hexo = require('hexo');

async function startServer() {
    const hexo = new Hexo(process.cwd(), {});
    hexo.env.init = true;
    await hexo.init();
    await hexo.load();
    await hexo.call('server', { port: 4000 });
    console.log("HEXO_SERVER_RUNNING_ON_PORT_4000");
}

startServer().catch(err => {
    console.error("SERVER_ERROR:", err);
});
