import logging

import fetch_sarasa as sarasa
from msyh_workflow import generate_ms_yahei
from project_utils import (clean_temp_dir, create_directories,
                           extract_custom_font_packages, get_config_value,
                           get_new_result_dir, load_config, validate_config)
from segoe_workflow import generate_segoe_ui

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


def main():
    config = load_config()
    try:
        logging.info("开始字体生成流程")
        validate_config(config)
        create_directories(config)
        # 获取所有源文件包或处理自定义包
        download_mode = get_config_value(config, 'FONT_PACKAGE_SOURCE', 'local')
        if get_config_value(config, 'ENABLE_MS_YAHEI', True):
            if download_mode == 'custom':
                # custom 模式下，解压自定义字体包到 temp 目录（仅支持 zip/7z）
                try:
                    extract_custom_font_packages(config)
                    logging.info("自定义字体包已全部解压到临时目录")
                except Exception as e:
                    logging.error(f"自定义字体包解压失败: {e}")
                    raise

                # 将 mapping 中的 otf 转为 ttf
                from project_utils import update_mapping_otf_to_ttf
                temp_dir = config.get('TEMP_DIR', './temp')
                if 'msyh_mapping' in config:
                    config['msyh_mapping'] = update_mapping_otf_to_ttf(config['msyh_mapping'], temp_dir, verbose=True)
                if 'segoe_mapping' in config:
                    config['segoe_mapping'] = update_mapping_otf_to_ttf(config['segoe_mapping'], temp_dir, verbose=True)

            elif download_mode == 'local':
                packages = sarasa.find_all_local_packages()
                if not packages:
                    logging.error("未找到任何本地源文件包，请检查 source_files 目录")
                    raise
                for pkg in packages:
                    logging.info(f"本地包: {pkg}")
                    sarasa.unzip(pkg)
            else:
                urls = sarasa.get_all_latest()
                if not urls:
                    logging.error("未找到任何可用的在线源文件包")
                    raise
                for url in urls:
                    path = sarasa.download(url, save_dir=get_config_value(config, 'SOURCE_FILES_DIR', './source_files'))
                    sarasa.unzip(path)
        # 生成唯一结果子目录
        result_subdir = get_new_result_dir(config)
        # 生成微软雅黑字体
        if get_config_value(config, 'ENABLE_MS_YAHEI', True):
            generate_ms_yahei(config, result_subdir)
        # 生成Segoe UI字体
        if get_config_value(config, 'ENABLE_SEGOE_UI', True):
            generate_segoe_ui(config, result_subdir)
        logging.info(f"所有字体生成完成，结果目录：{result_subdir}")
        # 自动清理 temp 目录（可选）
        if get_config_value(config, 'CLEAN_TEMP_ON_SUCCESS', False):
            clean_temp_dir(config)
    except Exception as e:
        logging.error(f"程序执行出错: {str(e)}")
        raise

if __name__ == '__main__':
    main()