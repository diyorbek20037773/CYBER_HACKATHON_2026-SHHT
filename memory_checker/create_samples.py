"""Run once to generate sample CSV files for the Streamlit app."""
import pandas as pd
import pickle, os

BASE_DIR  = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'models', 'feature_cols.pkl'), 'rb') as f:
    feat_cols = pickle.load(f)

BENIGN = {
    'pslist.nproc':45,'pslist.nppid':17,'pslist.avg_threads':10.56,
    'pslist.nprocs64bit':0,'pslist.avg_handlers':202.84,
    'dlllist.ndlls':1694,'dlllist.avg_dlls_per_proc':38.5,
    'handles.nhandles':9129,'handles.avg_handles_per_proc':212.30,
    'handles.nport':5,'handles.nfile':305,'handles.nevent':2418,
    'handles.ndesktop':12,'handles.nkey':880,'handles.nthread':494,
    'handles.ndirectory':130,'handles.nsemaphore':276,'handles.ntimer':48,
    'handles.nsection':242,'handles.nmutant':178,
    'ldrmodules.not_in_load':5,'ldrmodules.not_in_init':16,
    'ldrmodules.not_in_mem':2,'ldrmodules.not_in_load_avg':0.11,
    'ldrmodules.not_in_init_avg':0.36,'ldrmodules.not_in_mem_avg':0.04,
    'malfind.ninjections':0,'malfind.commitCharge':7,
    'malfind.protection':4,'malfind.uniqueInjections':0,
    'psxview.not_in_pslist':0,'psxview.not_in_eprocess_pool':0,
    'psxview.not_in_ethread_pool':0,'psxview.not_in_pspcid_list':0,
    'psxview.not_in_csrss_handles':12,'psxview.not_in_session':2,
    'psxview.not_in_deskthrd':26,'psxview.not_in_pslist_false_avg':0.0,
    'psxview.not_in_eprocess_pool_false_avg':0.0,
    'psxview.not_in_ethread_pool_false_avg':0.0,
    'psxview.not_in_pspcid_list_false_avg':0.0,
    'psxview.not_in_csrss_handles_false_avg':0.27,
    'psxview.not_in_session_false_avg':0.04,
    'psxview.not_in_deskthrd_false_avg':0.58,
    'modules.nmodules':147,'svcscan.nservices':364,
    'svcscan.kernel_drivers':221,'svcscan.fs_drivers':26,
    'svcscan.process_services':24,'svcscan.shared_process_services':116,
    'svcscan.interactive_process_services':0,'svcscan.nactive':121,
    'callbacks.ncallbacks':87,'callbacks.nanonymous':0,'callbacks.ngeneric':8,
}

RANSOMWARE = {
    'pslist.nproc':52,'pslist.nppid':21,'pslist.avg_threads':14.23,
    'pslist.nprocs64bit':0,'pslist.avg_handlers':312.50,
    'dlllist.ndlls':2100,'dlllist.avg_dlls_per_proc':42.3,
    'handles.nhandles':12500,'handles.avg_handles_per_proc':280.5,
    'handles.nport':8,'handles.nfile':890,'handles.nevent':3200,
    'handles.ndesktop':15,'handles.nkey':1200,'handles.nthread':620,
    'handles.ndirectory':180,'handles.nsemaphore':350,'handles.ntimer':62,
    'handles.nsection':310,'handles.nmutant':240,
    'ldrmodules.not_in_load':18,'ldrmodules.not_in_init':42,
    'ldrmodules.not_in_mem':12,'ldrmodules.not_in_load_avg':0.35,
    'ldrmodules.not_in_init_avg':0.81,'ldrmodules.not_in_mem_avg':0.23,
    'malfind.ninjections':8,'malfind.commitCharge':45,
    'malfind.protection':32,'malfind.uniqueInjections':6,
    'psxview.not_in_pslist':3,'psxview.not_in_eprocess_pool':2,
    'psxview.not_in_ethread_pool':1,'psxview.not_in_pspcid_list':2,
    'psxview.not_in_csrss_handles':28,'psxview.not_in_session':5,
    'psxview.not_in_deskthrd':42,'psxview.not_in_pslist_false_avg':0.06,
    'psxview.not_in_eprocess_pool_false_avg':0.04,
    'psxview.not_in_ethread_pool_false_avg':0.02,
    'psxview.not_in_pspcid_list_false_avg':0.04,
    'psxview.not_in_csrss_handles_false_avg':0.54,
    'psxview.not_in_session_false_avg':0.10,
    'psxview.not_in_deskthrd_false_avg':0.81,
    'modules.nmodules':162,'svcscan.nservices':398,
    'svcscan.kernel_drivers':235,'svcscan.fs_drivers':29,
    'svcscan.process_services':31,'svcscan.shared_process_services':134,
    'svcscan.interactive_process_services':2,'svcscan.nactive':138,
    'callbacks.ncallbacks':102,'callbacks.nanonymous':4,'callbacks.ngeneric':14,
}

samples_dir = os.path.join(BASE_DIR, 'samples')
os.makedirs(samples_dir, exist_ok=True)

pd.DataFrame([BENIGN])[feat_cols].to_csv(os.path.join(samples_dir, 'sample_benign.csv'), index=False)
pd.DataFrame([RANSOMWARE])[feat_cols].to_csv(os.path.join(samples_dir, 'sample_ransomware.csv'), index=False)
print('sample_benign.csv va sample_ransomware.csv yaratildi.')
