import os
model_path = "model/NELL-995.test-point.rs.new.conve-xavier-curriculum-200-200-3-0.003-0.1-0.1-0.1-256-0.05-3-{:.1f}-{}-0.1-useConf-3-0.9-test/model_best.tar"
command = "./experiment-newarch.sh configs/nell-995-newarch.sh --inference 0 --decrease_step {} --decrease_rate {} --checkpoint_path {} --save_beam_search_paths --test"
for step in range(5,15,5):
    for rate in [0.75, 0.8, 0.85, 0.9]:
        if rate == 0.85:
            continue
        d_rate = rate
        path = model_path.format(step, d_rate)
        shell_line = command.format(step, d_rate, path)
        os.system(shell_line)
