from pkg_resources import get_distribution, DistributionNotFound


def update_reqs():
    with open('requirements-to-freeze.txt') as f:
        reqs = [line.strip().split('==')[0] for line in f.readlines() if line.strip()]
    with open('requirements.txt') as f:
        reqs += [line.strip().split('==')[0] for line in f.readlines() if line.strip()]
    reqs = list(set(reqs))

    new_reqs = []
    problem_modules = []
    for r in reqs:
        try:
            version = get_distribution(r).version
        except DistributionNotFound:
            version = 'UNKNOWN_VERSION!!!...!!!...!!!'
            problem_modules.append(r)
        new_reqs.append(f"{r}=={version}")

    if problem_modules:
        print('\n\nPROBLEMS DETECTED!!!\n\nThe following modules will have to be updated manually:')
        for r in problem_modules:
            print(r)

        ans = input("\nContinue? (versions will be left blank for the above modules.) [y/n]")
        if ans.strip().lower() != 'y':
            print('Exiting early.  Nothing has been written.')
            return

    print('Writing...')
    with open('requirements-to-freeze.txt', 'w+') as f:
        f.write('\n'.join(sorted(reqs)))
    with open('requirements.txt', 'w+') as f:
        f.write('\n'.join(sorted(new_reqs)))
    print('Requirement files updated successfully.')


if __name__ == '__main__':
    ans = input('Have you updated your environment to have the desired package versions?  (y/n)')
    if ans.strip().lower() == 'y':
        update_reqs()
    else:
        print('Nothing updated, per your answer.')
