const Hexo = require('hexo');

async function build() {
    const hexo = new Hexo(process.cwd(), {});
    await hexo.init();
    await hexo.load();
    await hexo.call('generate', {});
    console.log("HEXO_BUILD_COMPLETED_SUCCESSFULLY");
}

build().catch(err => {
    console.error("BUILD_ERROR:", err);
    process.exit(1);
});
